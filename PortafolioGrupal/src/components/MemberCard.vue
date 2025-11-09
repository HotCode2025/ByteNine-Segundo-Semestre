<template>
  <div class="member-card" @click="$emit('member-click', member.id)">
    <div class="card-glow"></div>
    <img :src="member.avatar" :alt="member.name" class="member-photo">
    <h2 class="member-name">{{ member.name }}</h2>
    <p class="member-role">{{ member.role }}</p>
    <p class="member-email">{{ member.email }}</p>
    <p class="member-quote">"{{ member.quote }}"</p>
    <div class="card-hover-effect"></div>
  </div>
</template>

<script>
export default {
  name: 'MemberCard',
  props: {
    member: {
      type: Object,
      required: true
    }
  },
  emits: ['member-click']  // Declaramos el evento que emitimos
}
</script>



<style scoped>
.member-card {
  background: linear-gradient(145deg, #1e1e2e 0%, #252536 100%);
  border-radius: 15px;
  padding: 2rem;
  text-align: center;
  border: 1px solid #333;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  position: relative;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.card-glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, #64b5f6, #2196f3, #64b5f6);
  background-size: 200% 100%;
  animation: glow 3s infinite;
}

@keyframes glow {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

.member-card:hover {
  transform: translateY(-10px) scale(1.02);
  border-color: #64b5f6;
  box-shadow: 0 15px 40px rgba(33, 150, 243, 0.3);
}

.member-photo {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 1.5rem;
  border: 3px solid #64b5f6;
  box-shadow: 0 0 20px rgba(33, 150, 243, 0.3);
  transition: all 0.3s ease;
}

.member-card:hover .member-photo {
  border-color: #2196f3;
  box-shadow: 0 0 30px rgba(33, 150, 243, 0.5);
  transform: scale(1.1);
}

.member-name {
  font-size: 1.5rem;
  color: #ffffff;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.member-role {
  font-size: 1.1rem;
  color: #64b5f6;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.member-email {
  color: #b0b0b0;
  margin-bottom: 1rem;
  font-size: 0.9rem;
}

.member-quote {
  font-style: italic;
  color: #e0e0e0;
  border-left: 3px solid #64b5f6;
  padding-left: 1rem;
  margin-top: 1rem;
  font-size: 0.95rem;
}

.card-hover-effect {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(100, 181, 246, 0.1), transparent);
  transition: left 0.6s ease;
}

.member-card:hover .card-hover-effect {
  left: 100%;
}
</style>