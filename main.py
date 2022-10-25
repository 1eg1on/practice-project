#!/usr/bin/env python3


if __name__ == '__main__':

    import sys
    import useful_package
    from useful_package import module_a, module_b
    
    x = int(sys.argv[1])
    print(f'x: {x}')
    print(f'cube: {module_a.polynom_3(x)}')
    print(f'hyperbola: {module_b.hyperbola(x)}')

