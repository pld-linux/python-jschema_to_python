#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Generate Python classes from a JSON schema
Summary(pl.UTF-8):	Generowanie klas pythonowych ze schematu JSON
Name:		python-jschema_to_python
Version:	1.2.3
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/jschema-to-python/
Source0:	https://files.pythonhosted.org/packages/source/j/jschema-to-python/jschema_to_python-%{version}.tar.gz
# Source0-md5:	6f9e312084eafe0f33fcb0cf768ab25e
URL:		https://pypi.org/project/jschema-to-python/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-attrs
BuildRequires:	python-jsonpickle
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-pbr
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-attrs
BuildRequires:	python3-jsonpickle
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generate source code for Python classes from a JSON schema.

%description -l pl.UTF-8
Generowanie kodu źródłowego klas w Pythonie ze schematu JSON.

%package -n python3-jschema_to_python
Summary:	Generate Python classes from a JSON schema
Summary(pl.UTF-8):	Generowanie klas pythonowych ze schematu JSON
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-jschema_to_python
Generate source code for Python classes from a JSON schema.

%description -n python3-jschema_to_python -l pl.UTF-8
Generowanie kodu źródłowego klas w Pythonie ze schematu JSON.

%prep
%setup -q -n jschema_to_python-%{version}

# fix tests on UNIX
%{__sed} -i -e 's/\r$//' tests/test_files/*.py

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README.rst SECURITY.md
%{py_sitescriptdir}/jschema_to_python
%{py_sitescriptdir}/jschema_to_python-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-jschema_to_python
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README.rst SECURITY.md
%{py3_sitescriptdir}/jschema_to_python
%{py3_sitescriptdir}/jschema_to_python-%{version}-py*.egg-info
%endif
