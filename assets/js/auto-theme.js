/** Theme switcher based on user preferences */

const query = window.matchMedia('(prefers-color-scheme: dark)')
const target = document.querySelector('html')

const update = ({ matches }) => {
    target.dataset.bsTheme = matches ? 'dark' : 'light'
}

update(query)
query.addEventListener('change', update)
