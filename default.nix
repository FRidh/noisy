{ buildPythonPackage
, numpy
}:

buildPythonPackage rec {
  name = "noisy-${version}";
  version = "dev";

  src = ./.;

  propagatedBuildInputs = [ numpy ];

  # No tests
  doCheck = false;
}
