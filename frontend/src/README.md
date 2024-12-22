## Structure of folders 

```
─ App.css
├── App.tsx
├── README.md
├── components
│   ├── README.md
│   ├── alert.tsx
│   ├── avatar.tsx
│   ├── badge.tsx
│   ├── button.tsx
│   ├── checkbox.tsx
│   ├── description-list.tsx
│   ├── dialog.tsx
│   ├── divider.tsx
│   ├── dropdown.tsx
│   ├── fieldset.tsx
│   ├── heading.tsx
│   ├── input.tsx
│   ├── link.tsx
│   ├── listbox.tsx
│   ├── navbar.tsx
│   ├── pagination.tsx
│   ├── preferences.tsx
│   ├── radio.tsx
│   ├── select.tsx
│   ├── sidebar-layout.tsx
│   ├── sidebar.tsx
│   ├── stacked-layout.tsx
│   ├── switch.tsx
│   ├── table.tsx
│   ├── text.tsx
│   └── textarea.tsx
├── index.css
├── main.tsx
├── pages
│   └── WordHunt.tsx
├── util
│   ├── data.ts
│   └── helpers.ts
└── vite-env.d.ts
```

## Explanation of the structure

- `App.css` and `index.css` are the global stylesheets for the app.
- `App.tsx` is the main component of the app. If you want to edit the routes or the layout of the app, you can do it here.
- `components` folder contains components from Catalyst Tailwind UI. I didn't use them in this basic project, but if you want to use them, you can find the documentation for them [here](https://catalyst.tailwindui.com/docs). In the future you should probably refactor out the straight tsx in `WordHunt.tsx` into these components.
- `main.tsx` is the entry point of the app. Don't edit this file unless you know what you are doing.
- `pages` folder contains the pages of the app. In this case, there is only one page called `WordHunt.tsx`.
- `util` folder contains the data and helper functions for the app.
- `vite-env.d.ts` is the TypeScript declaration file for Vite.

