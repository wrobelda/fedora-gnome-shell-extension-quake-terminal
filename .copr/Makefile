.PHONY: srpm

srpm:
	dnf -y install rpm-build rpmdevtools rpmautospec git-core
	mkdir -p "$(outdir)"
	spectool -g -C "$(CURDIR)" "gnome-shell-extension-quake-terminal.spec"
	sha512sum --check sources
	rpmautospec process-distgit "gnome-shell-extension-quake-terminal.spec" "$(outdir)/gnome-shell-extension-quake-terminal.spec"
	rpmbuild -bs "$(outdir)/gnome-shell-extension-quake-terminal.spec" --define "_sourcedir $(CURDIR)" --define "_srcrpmdir $(abspath $(outdir))"

