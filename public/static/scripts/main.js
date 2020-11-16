var currentTheme = localStorage.getItem("theme");
if (currentTheme == "dark") {
  document.documentElement.setAttribute("data-theme", "dark");
} 

function toggleTheme() {
    let new_theme = currentTheme == 'dark'? 'light' : 'dark'
    trans()
    document.documentElement.setAttribute('data-theme', new_theme)
    localStorage.setItem("theme", new_theme);
    currentTheme = new_theme;
}

let trans = () => {
    document.documentElement.classList.add('transition');
    window.setTimeout(() => {
        document.documentElement.classList.remove('transition')
    }, 1000)
}