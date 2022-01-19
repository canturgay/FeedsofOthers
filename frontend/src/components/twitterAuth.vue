<template>
  <div>
    <h1>Feeds of Others</h1>
    <p>Log-in with twitter</p>
    <button @click="getAuth">Log-in with Twitter</button>
    <p>{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'twitterAuth',
  data () {
    return {
      message: undefined,
      token: undefined,
      secret: undefined,
    }
  },
  methods: {
    getAuth () {
      const path = 'http://127.0.0.1:5000/auth/check'
      axios.get(path)
        .then(response => {
          if (response.status === 200) {
            this.$store.commit('setToken', response.data.oauth_token),
            this.$store.commit('setSecret', response.data.oauth_token_secret)
            this.message = response.data
          }
          else if (response.status === 201) {
            window.location.href = 'http://127.0.0.1:5000/auth/twitter'
          }
        })
        .catch(error => {
          console.log(error)
        })
    },
  }}
</script>