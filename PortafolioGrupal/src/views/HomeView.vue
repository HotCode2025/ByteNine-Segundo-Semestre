<template>
  <div class="home-view">
    <div class="container">
      <TeamGrid />
    </div>
  </div>
</template>

<script>
import TeamGrid from '@/components/TeamGrid.vue'

export default {
  name: 'HomeView',
  components: {
    TeamGrid
  }
}
</script>