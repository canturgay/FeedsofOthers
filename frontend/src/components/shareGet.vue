<template>
  <div>
    <h1>Feeds of Others</h1>
    <p>Share & Get</p>
    <input v-model="self_tags" placeholder="Enter your tags separated by comma">
    <button @click="share">Share</button>
    <input v-model="lookup_tag" placeholder="Enter the tag you want to see the feed of">
    <button @click="get">Get</button>
    <p>{{ gotten_tweets }}</p>
  </div>

</template>

<script>
import axios from 'axios'

export default {
  name: 'shareGet',
  data () {
    return {
      message: undefined,
      self_tags: this.$store.state.tags,
      self_tweets: undefined,
      gotten_tweets: undefined,
      lookup_tag: undefined
    }
  },
  methods: {
    share () {
      const path = 'http://127.0.0.1:5000/share/'
      axios.post(path, {
        params: {
          tags: this.self_tags
        }
      })
        .then(response => {
          this.self_tweets = response
        })
        .catch(error => {
          console.log(error)
        })
    },
    get () {
      const path = 'http://127.0.0.1:5000/get/'
      axios.get(path, {
        params: {
          lookup_tag: this.lookup_tag
        }
      })
        .then(response => {
          this.gotten_tweets = response
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>