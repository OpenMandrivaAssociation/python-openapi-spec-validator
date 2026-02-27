Name:		python-openapi-spec-validator
Version:	0.8.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/o/openapi_spec_validator/openapi_spec_validator-%{version}.tar.gz
Summary:	OpenAPI 2.0 (aka Swagger) and OpenAPI 3 spec validator
URL:		https://pypi.org/project/openapi_spec_validator/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
OpenAPI 2.0 (aka Swagger) and OpenAPI 3 spec validator

%files
%{_bindir}/openapi-spec-validator
%{py_sitedir}/openapi_spec_validator
%{py_sitedir}/openapi_spec_validator-*.*-info
