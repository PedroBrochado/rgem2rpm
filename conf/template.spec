%define distnum %{expand:%%(/usr/lib/rpm/redhat/dist.sh --distnum)}
%define disttype %{expand:%%(/usr/lib/rpm/redhat/dist.sh --disttype)}
%define name <%=name%>
%define version <%=version%>
%define release <%=rpm_release%>.%{disttype}%{distnum}

Name: %{name}
Version: %{version}
Release: %{release}
License: See <%=homepage%>
Summary: <%=summary%>
Group: <%=rpm_group%>
Source: %{name}-%{version}.tar.gz
Prefix: <%=os_install_dir%>
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
<%="BuildArch: noarch" if rpm_no_arch%>
<%="Requires: #{requires}" unless requires.nil?%>
%description
<%=description%>

%prep
%setup -q

%install
<%=rpm_install%>

<%="%post\n#{rpm_post}" unless rpm_post.nil?%>

%postun
rm -rf %{prefix}/gems/%{name}-%{version}

%files
%defattr(-,<%=os_user%>,<%=os_group%>)
<%=files%>
