<script setup>
import { ref } from 'vue'

const count = ref(0)

function increment(){
	count.value++
}
  
// const increment = () => count.value++
  
</script>

<template>
  <!-- 使此按钮生效 -->
  <button @click="increment">count is: {{ count 
    }}
  </button>
</template>