<template>
  <div id="app">
    <textarea v-model="req"/><br />
    <button @click="onclick">検索</button>
    <ul>
      <li v-for="event in state.events">{{event}}</li>
    </ul>
  </div>
</template>

<script>
import store from './store';

export default {
  name: 'app',
  data() {
    return {
      state: store.state,
      req: '{}',
    };
  },
  created() {
    store.listenEvents();
  },
  methods: {
    onclick() {
      store.clearEvents();
      store.sendRequest(this.req);
      this.req = '{}';
    },
  },
};
</script>

<style>
textarea {
  width: 300px;
  height: 100px;
}
</style>
