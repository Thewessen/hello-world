import React from 'react'

const Dialog = React.lazy(() => import('app_two_remote/Dialog'))

const Page1 = () => (
  <div>
    <h1>Hello from App1</h1>
    <React.Suspense fallback="loading...">
      <Dialog />
    </React.Suspense>
  </div>
)

export default Page1
