import { rest } from 'msw'

export default [
  rest.get('/network', (req, res, ctx) => {
    return res(
      ctx.json({
        network: 'Mock network works! :)'
      })
    )
  }),
  rest.get('/memberGraph', (req, res, ctx) => {
    return res(ctx.json(memberGraph))
  }),
  rest.get('/usernames', (req, res, ctx) => {
    return res(ctx.json(usernames))
  }),
  rest.get('/userDetails/:username', (req, res, ctx) => {
    return res(ctx.json(userDetails))
  }),
  rest.get('/activities', (req, res, ctx) => {
    return res(ctx.json(activities))
  }),
]

const memberGraph = {
  nodes: [
    { id: 1,  label: 'njonjo',  shape: 'image', image: "https://avatars.githubusercontent.com/u/4950251?s=88&v=4", borderWidth: 10, color: { border: 'green' }, },
    { id: 2,  label: 'ellipse', shape: 'ellipse', borderWidth: 5, color: { border: 'green' } },
    { id: 3,  label: 'database', shape: 'database' },
    { id: 4,  label: 'njonjo2', image: 'https://avatars.githubusercontent.com/u/4950251?s=88&v=4' },
    { id: 5,  label: 'diamond', shape: 'diamond' },
    { id: 6,  label: 'dot',     shape: 'dot' },
    { id: 7,  label: 'square',  shape: 'square' },
    { id: 8,  label: 'triangle',shape: 'triangle' },
  ],
  edges: [
    {from: 1, to: 2},
    {from: 2, to: 3},
    {from: 2, to: 4},
    {from: 2, to: 5}, 
    {from: 5, to: 6},
    {from: 5, to: 7},
    {from: 6, to: 8}
  ]
}

const usernames = {
  usernames: [
    "Gitbuda",
    "afico",
    "jmrden",
    "jmatak",
  ]
}

const userDetails = {
  username: "Gitbuda",
  firstName: "Marko",
  lastname: "Budiselic",
  love: 10.2,
  avatar: "https://avatars.githubusercontent.com/u/4950251?s=88&v=4",
  community: "Feature, not bug",
  importance: 50.5,
  company: "Memgraph"
}

const activities = {
  activities: [
    {
      username: "Gitbuda",
      action: "PR_MAKE",
      description: "This guy made a PR!",
      date: "2020-01-01T08:00:00",
    },
    {
      username: "Gitbuda2",
      action: "PR_MAKE2",
      description: "This guy made a PR!",
      date: "2020-01-01T08:00:00",
    },
    {
      username: "Gitbuda3",
      action: "PR_MAKE3",
      description: "This guy made a PR!",
      date: "2020-01-01T08:00:00",
    },
    {
      username: "Gitbuda",
      action: "PR_MAKE",
      description: "This guy made a PR!",
      date: "2020-01-01T08:00:00",
    },
    {
      username: "Gitbuda2",
      action: "PR_MAKE2",
      description: "This guy made a PR!",
      date: "2020-01-01T08:00:00",
    },
    {
      username: "Gitbuda3",
      action: "PR_MAKE3",
      description: "This guy made a PR!",
      date: "2020-01-01T08:00:00",
    },
    {
      username: "Gitbuda",
      action: "PR_MAKE",
      description: "This guy made a PR!",
      date: "2020-01-01T08:00:00",
    },
    {
      username: "Gitbuda2",
      action: "PR_MAKE2",
      description: "This guy made a PR!",
      date: "2020-01-01T08:00:00",
    },
    {
      username: "Gitbuda3",
      action: "PR_MAKE3",
      description: "This guy made a PR!",
      date: "2020-01-01T08:00:00",
    },
    {
      username: "Gitbuda",
      action: "PR_MAKE",
      description: "This guy made a PR!",
      date: "2020-01-01T08:00:00",
    },
    {
      username: "Gitbuda2",
      action: "PR_MAKE2",
      description: "This guy made a PR!",
      date: "2020-01-01T08:00:00",
    },
    {
      username: "Gitbuda3",
      action: "PR_MAKE3",
      description: "This guy made a PR!",
      date: "2020-01-01T08:00:00",
    },
  ]
}

