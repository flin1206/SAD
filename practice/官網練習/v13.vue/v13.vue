<script setup>
import { ref } from 'vue'
import ChildComp from './ChildComp.vue'

const childMsg = ref('No child msg yet')

const responseHandler = (msg)=> {
  childMsg.value = msg
}
</script>

<template>
  <ChildComp @response="responseHandler"/>
  <p>{{ childMsg }}</p>
</template>