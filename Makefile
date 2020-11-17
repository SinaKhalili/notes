serve-and-watch:
	browser-sync public -w --port 8000 &
	watch  -n 5 python build.py

serve:
	browser-sync public -w --port 8000

watch:
	watch -n 6 python build.py 

watch-closely:
	ls *.py *.md templates/_base.html templates/index.html templates/page.html static/*/* | entr python build.py

prod:
	BUILD_ENV=deploy python build.py
