import filecmp
import pytest

from duf_extraction.duf_processing import Processing

EMAIL = "raven.neo@gmail.com"
INPUT_FILE = "./tests/resources/sample_protein_file.csv"
AFA_OUTPUT_DIR = "./output"

def getProteins():
    proteins = ['WP_014055290.1', 'WP_030630441.1', 'WP_031074839.1', 'WP_033304178.1',
        'WP_076970707.1', 'EMP10873.2', 'WP_033540164.1', 'WP_036292654.1', 'WP_039412518.1',
        'WP_052663444.1', 'WP_060921984.1', 'WP_062633540.1', 'WP_071328144.1', 'WP_073384391.1']
    return proteins

def test_get_proteins():
    processing_protein = Processing(INPUT_FILE, AFA_OUTPUT_DIR, EMAIL)
    proteins = processing_protein.get_proteins()
    assert len(proteins) == 14
    assert proteins == getProteins()

def test_get_proteins_with_duplicates():
    input_csv_file = "./tests/resources/file_with_duplicates.csv"
    processing_protein = Processing(input_csv_file, AFA_OUTPUT_DIR, EMAIL)
    proteins = processing_protein.get_proteins()
    assert len(proteins) == 14
    assert proteins == getProteins()

def test_muscle():
    processing_protein = Processing(INPUT_FILE, AFA_OUTPUT_DIR, EMAIL)
    processing_protein.muscle_protein()
    filecmp.cmp("./output/sample_protein_file.afa", "./tests/resources/sample_protein_file.afa")
