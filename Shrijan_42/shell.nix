{ pkgs ? import <nixpkgs> {} }:

let
  pythonEnv = pkgs.python3.withPackages (ps: with ps; [
    numpy
    sympy
  ]);
in

pkgs.mkShell {
  name = "numerical-methods-shell";

  buildInputs = [
    pkgs.git
    pkgs.curl
    pkgs.jq
    pythonEnv
  ];

  shellHook = ''
    echo "Numerical Methods dev shell (Python + numpy + sympy)"
  '';
}
