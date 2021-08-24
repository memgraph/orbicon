import { rest } from 'msw'

export default [
  rest.get('/message', (req, res, ctx) => {
    return res(
      ctx.json({
        message: 'Mock data works! :)'
      })
    )
  }),
  rest.get('/network', (req, res, ctx) => {
    return res(
      ctx.json({
        network: 'Mock network works! :)'
      })
    )
  }),
  rest.get('/nodes', (req, res, ctx) => {
    return res(ctx.json(nodes))
  }),
  rest.get('/links', (req, res, ctx) => {
    return res(ctx.json(links))
  }),
]


const nodes = {
  nodes: [
    { id: 1,  label: 'njonjo',  shape: 'image', image: "https://avatars.githubusercontent.com/u/4950251?s=88&v=4", borderWidth: 10, color: { border: 'green' }, },
    { id: 2,  label: 'ellipse', shape: 'ellipse', borderWidth: 5, color: { border: 'green' } },
    { id: 3,  label: 'database', shape: 'database' },
    { id: 4,  label: 'njonjo2', image: 'https://avatars.githubusercontent.com/u/4950251?s=88&v=4' },
    { id: 5,  label: 'diamond', shape: 'diamond' },
    { id: 6,  label: 'dot',     shape: 'dot' },
    { id: 7,  label: 'square',  shape: 'square' },
    { id: 8,  label: 'triangle',shape: 'triangle' },
  ]
}

const links = { 
  links: [
    {from: 1, to: 2},
    {from: 2, to: 3},
    {from: 2, to: 4},
    {from: 2, to: 5}, 
    {from: 5, to: 6},
    {from: 5, to: 7},
    {from: 6, to: 8}
  ]
}