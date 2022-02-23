#!/usr/bin/env python3

import os
import re


def main() -> None:
    base_ref = os.environ.get('GITHUB_BASE_REF')
    ref = os.environ['GITHUB_REF']
    m = re.match(r'^refs/(\w+)/(.*)$', ref)
    if m:
        category, stripped = m.groups()
        if category == 'heads':
            print(f'::set-output name=branch::{stripped}')
        elif category == 'pull':
            print(f'::set-output name=branch::pull/{stripped.split("/")[0]}')
        elif category == 'tags':
            print(f'::set-output name=tag::{stripped}')

    if base_ref:
        print(f'::set-output name=base_ref::{base_ref}')


if __name__ == '__main__':
    main()
