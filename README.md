# Web2py + Svelte Demo

Demo to integrate a [web2py](http://web2py.com/book) backend with a [Svelte](https://svelte.dev/docs) frontend.

## Requirements
- python 3.6+ with [web2py](http://www.web2py.com/init/default/download)
- nodejs with npm

## Installation
- Python: throw this project in your web2py applications folder
- Svelte: (from the `views/svelte` folder) run `npm install` and `npm run dev` (for development, live builds) or `npm run build` (for producting, manual builds)

## Props/data
All data that you return in the controller, will be passed as 'props' to the frontend page. This means you can use them as js variables.
### example:
if you return `{'name': 'World', 'value': 15}` in a controller, you can use those values like:
```js
export let name; // this will get the value World
export let value; // this will get the value 15
```
Because of this feature, you always have to return a dictionary at the end of each controller.

## Routing
Svelte is normally used for single-page applications (SPA), but there are multiple ways to use it with multiple pages:
- Making multiple files like `main.js`, where you instantiate the right Component for that page (lot of manual work)
- Using a routing library like `svelte-routing` to show a Component based on the current URL. This works best for an app without backend, but when using a backend you have to define your routes twice.
- *Providing a `view` variable in the backend and using that to dynamically show the right component. This is the approach I took in this demo.
  * If you want to add a new front-end page, you first have to make a Svelte page in `src/pages` and then import it and add it to the components object in `main.js`
  * You can use choose the page for a controller function with the `@svelte` decorator defined in `models/svelte`.
  ```python
  @svelte('Alternate')
  def alternative_frontend():
      # this page will be using the Alternate.svelte page
      return {}
  ```

## Demo pages
- default/index shows that you can give information from the backend to the front-end
- default/page2 
- default/non_svelte shows that you can show pages without svelte

## TODO:
- Use the web2py bootstrap css/js