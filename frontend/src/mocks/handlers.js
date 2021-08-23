import { rest } from 'msw'

export default [
  rest.get('/message', (req, res, ctx) => {
    return res(
      ctx.json({
        message: 'Mock data works! :)'
      })
    )
  })
]