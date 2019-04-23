from tests.utils import get_specfile
    spec = get_specfile(str(distgit / "beer.spec"))
def test_basic_local_update_empty_patch(
    spec = get_specfile(str(distgit / "beer.spec"))
    assert "# PATCHES FROM SOURCE GIT" not in spec_package_section
    assert not spec.patches["applied"]
    assert not spec.patches["not_applied"]
    spec = get_specfile(str(distgit / "beer.spec"))
    assert "Patch0002: 0002" not in spec_package_section  # no empty patches
