<template>
  <footer class="main-footer">
    <div class="container">
      <p class="footer-text">© 2025 ByteNine - Todos los derechos reservados</p>
    </div>
  </footer>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names, vue/no-reserved-component-names
  name: 'Footer'
}
</script>

<style scoped>
.main-footer {
  background: linear-gradient(135deg, rgba(23, 23, 36, 0.95) 0%, rgba(30, 30, 48, 0.95) 100%);
  color: #b0b0b0;
  text-align: center;
  padding: 2rem 0;
  margin-top: 4rem;
  border-top: 1px solid #333;
  backdrop-filter: blur(10px);
}

.footer-text {
  font-size: 1rem;
  letter-spacing: 1px;
}
</style>