%global uuid quake-terminal@diegodario88.github.io
%global extdir %{_datadir}/gnome-shell/extensions/%{uuid}

Name:           gnome-shell-extension-quake-terminal
Version:        1.4.0
Release:        %autorelease
Summary:        Drop-down terminal wrapper for GNOME Shell

License:        GPL-3.0-or-later
URL:            https://github.com/diegodario88/quake-terminal
Source0:        %{url}/archive/v%{version}/quake-terminal-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  glib2
Requires:       gnome-shell >= 45
Requires:       libadwaita

%description
Shows and hides a terminal window with a keyboard shortcut.
It supports configurable window size, position, animation, and monitor
selection.

%prep
%autosetup -n quake-terminal-%{version}
# Rebuild translations and use the system schema cache.
find src -name '*.mo' -delete
rm -f src/schemas/gschemas.compiled

%build
for po in src/po/*.po; do
    msgfmt "$po" -o "${po%.po}.mo"
done

%install
install -d %{buildroot}%{extdir}
install -pm0644 src/*.js src/metadata.json %{buildroot}%{extdir}/
install -Dpm0644 src/schemas/org.gnome.shell.extensions.quake-terminal.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.quake-terminal.gschema.xml
for mo in src/po/*.mo; do
    lang=$(basename "$mo" .mo)
    install -Dpm0644 "$mo" %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/%{uuid}.mo
done
%find_lang %{uuid}

%check
glib-compile-schemas --strict --dry-run src/schemas

%files -f %{uuid}.lang
%license LICENSE
%doc README.md
%{extdir}/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.quake-terminal.gschema.xml

%changelog
%autochangelog
