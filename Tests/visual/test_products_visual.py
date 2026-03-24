import pytest
from PIL import Image, ImageChops

from Core.paths import ensure_dir
from Services.products_page import OpenProductsPage


def _images_are_equal(img_a: Image.Image, img_b: Image.Image, diff_threshold: int = 0) -> bool:
    diff = ImageChops.difference(img_a, img_b)
    bbox = diff.getbbox()
    if bbox is None:
        return True
    # Any non-zero diff counts unless threshold is set.
    return diff_threshold > 0


@pytest.mark.visual
def test_products_page_visual_baseline(driver, settings):
    page = OpenProductsPage(driver)
    page.open_products_page()

    baseline_dir = ensure_dir("Artifacts/visual_baseline")
    actual_dir = ensure_dir("Artifacts/visual_actual")

    baseline_path = baseline_dir / "products_page.png"
    actual_path = actual_dir / "products_page.png"

    driver.save_screenshot(str(actual_path))

    if not baseline_path.exists():
        # First run creates baseline and skips comparison.
        driver.save_screenshot(str(baseline_path))
        pytest.skip("Baseline created. Re-run to compare.")

    img_baseline = Image.open(baseline_path)
    img_actual = Image.open(actual_path)

    assert _images_are_equal(img_baseline, img_actual), "Visual regression detected"
