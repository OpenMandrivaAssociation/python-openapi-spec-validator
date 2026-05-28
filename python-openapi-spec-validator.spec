%define module openapi-spec-validator
%define oname openapi_spec_validator

Name:		python-openapi-spec-validator
Version:	0.9.0
Release:	1
Summary:	OpenAPI 2.0 (aka Swagger) and OpenAPI 3 spec validator
License:	None
Group:		Development/Python
URL:		https://pypi.org/project/openapi_spec_validator
Source0:	https://files.pythonhosted.org/packages/source/o/%{oname}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
OpenAPI 2.0 (aka Swagger) and OpenAPI 3 spec validator

%files
%{_bindir}/%{module}
%{py_sitedir}/%{oname}
%{py_sitedir}/%{oname}-%{version}.dist-info
