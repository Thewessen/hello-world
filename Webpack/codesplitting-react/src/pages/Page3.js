import React from 'react'
import { get, capitalize } from 'lodash'
import moment from 'moment'

const Page3 = () => (
  <div>
    <h1>{capitalize(get({ a: { name: 'page 3' }}, 'a.name'))}</h1>
    <p>
      Current date: {moment().format('DD-MM-YYYY HH:MM')}
    </p>
    <p>
      Dolor ea est obcaecati laboriosam fugit Quo voluptate excepturi obcaecati et assumenda Eos odit totam ipsa corrupti eum cumque Dolorem laudantium voluptas quo distinctio quisquam, sunt Eaque quo in sed
    </p>
  </div>
)

export default Page3
