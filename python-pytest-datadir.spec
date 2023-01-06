#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	pytest plugin for test data directories and files
Summary(pl.UTF-8):	Wtyczka pytesta do katalogów i plików z danymi testowymi
Name:		python-pytest-datadir
# keep 1.3.x here for python2 support
Version:	1.3.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-datadir/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-datadir/pytest-datadir-%{version}.tar.gz
# Source0-md5:	b63756178be5133515f48f7586dacb9b
URL:		https://pypi.org/project/pytest-datadir/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest >= 2.7.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 2.7.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pytest plugin for manipulating test data directories and files.

%description -l pl.UTF-8
Wtyczka pytesta do operowania na katalogach i plikach z danymi
testowymi.

%package -n python3-pytest-datadir
Summary:	pytest plugin for test data directories and files
Summary(pl.UTF-8):	Wtyczka pytesta do katalogów i plików z danymi testowymi
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-pytest-datadir
pytest plugin for manipulating test data directories and files.

%description -n python3-pytest-datadir -l pl.UTF-8
Wtyczka pytesta do operowania na katalogach i plikach z danymi
testowymi.

%prep
%setup -q -n pytest-datadir-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_datadir.plugin" \
PYTHONPATH=$(pwd)/src \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_datadir.plugin" \
PYTHONPATH=$(pwd)/src \
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
%doc AUTHORS CHANGELOG.rst LICENSE README.md
%{py_sitescriptdir}/pytest_datadir
%{py_sitescriptdir}/pytest_datadir-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-datadir
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG.rst LICENSE README.md
%{py3_sitescriptdir}/pytest_datadir
%{py3_sitescriptdir}/pytest_datadir-%{version}-py*.egg-info
%endif
