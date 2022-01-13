<template>
  <div>
    <h1>Feeds of Others</h1>
    <p>Log-in with twitter</p>
    <button @click="getAuth">Log-in with Twitter</button>
    <button @click="shareLoad">Share&Load</button>
  
    <p>{{ message }}</p>
  </div>

</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      message: '',
      tags: [],
      token: '',
      secret: '',
    }
  },
  methods: {
    getAuth () {
      const path = 'http://127.0.0.1:5000/auth'
      axios.get(path)
        .then(response => {
          if (response.status === 200) {
            this.token = response.data.oauth_token
            this.secret = response.data.oauth_token_secret
            this.message = 'Logged-in with Twitter'
          }
          else if (response.status === 201) {
            window.location.href = 'http://127.0.0.1:5000/auth/twitter' 
          }
        })
        .catch(error => {
          console.log(error)
        })
    },

    shareLoad () {
      const path = 'https://api.twitter.com/1.1/statuses/home_timeline.json?tweet_mode=extended'
      const config = {
        headers: {
          Authorization: 'Bearer ' + this.token,
          'Content-Type': 'application/json'
        }
      }
      axios.get(path, config)
        .then(response => {
          if (response.status === 200) {
            this.message = response.data.full_text
          }
        })
        .catch(error => {
          console.log(error)
        })
  },
}}
</script>