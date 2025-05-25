import pytest
from localization import t, TRANSLATIONS, LANGUAGES

def test_translation_basic():
    assert t("THOUGHT", "en") == "Thought"
    assert t("THOUGHT", "ru") == "Мысль"
    assert t("ID", "en") == "ID"
    assert t("ID", "ru") == "ID"
    assert t("NonexistentKey", "en") == "NonexistentKey"
    assert t("NonexistentKey", "ru") == "NonexistentKey"

def test_all_keys_present():
    en_keys = set(TRANSLATIONS["en"].keys())
    ru_keys = set(TRANSLATIONS["ru"].keys())
    # Check that all keys are present in both languages
    assert en_keys == ru_keys

def test_language_fallback():
    # If language is not supported, English should be used
    assert t("THOUGHT", "de") == "Thought"
    assert t("ID", "fr") == "ID"

def test_all_languages_supported():
    for lang in LANGUAGES:
        for key in TRANSLATIONS["en"].keys():
            assert key in TRANSLATIONS[lang]