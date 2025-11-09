<template>
  <header class="main-header">
    <div class="container">
      <h1>BYTENINE</h1>
      <p class="tagline">Soluciones Digitales de Clase Mundial</p>
    </div>
  </header>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names, vue/no-reserved-component-names
  name: 'Header'
}
</script>

<style scoped>
.main-header {
  background: linear-gradient(135deg, rgba(23, 23, 36, 0.95) 0%, rgba(30, 30, 48, 0.95) 100%);
  color: white;
  padding: 3rem 0;
  text-align: center;
  margin-bottom: 2rem;
  border-bottom: 1px solid #333;
  backdrop-filter: blur(10px);
}

.main-header h1 {
  font-size: 3.5rem;
  font-weight: 700;
  letter-spacing: 6px;
  margin-bottom: 0.5rem;
  background: linear-gradient(45deg, #64b5f6, #2196f3);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.tagline {
  font-size: 1.2rem;
  color: #b0b0b0;
  font-weight: 300;
  letter-spacing: 2px;
}
</style>