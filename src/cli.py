import argparse
import sys

from cpf.generator import generate_cpf
from cpf.validator import validate_cpf


def main():
    parser = argparse.ArgumentParser(
        description='CPF Generator and Validator CLI'
    )
    subparsers = parser.add_subparsers(dest='command')
    
    generate_parser = subparsers.add_parser(
        'generate', help='Generate a valid CPF'
    )
    generate_parser.add_argument(
        '--raw', action='store_true', help='Generate without formatting'
    )
    
    validate_parser = subparsers.add_parser(
        'validate', help='Validate a given CPF'
    )