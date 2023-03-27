<script setup>
import { ref, onMounted } from 'vue'

const p = ref(null)

onMounted(()=>{
  
  p.value.textContent = "123"
})
</script>

<template>
  <p ref="p">hello</p>
</template>