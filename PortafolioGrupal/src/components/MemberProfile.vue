<template>
  <section class="profile-section" v-if="member">
    <div class="profile-header">
      <img :src="member.avatar" :alt="member.name">
      <div class="profile-info">
        <h2>{{ member.name }} <span>{{ member.role }}</span></h2>
        <p class="member-quote">"{{ member.quote }}"</p>
      </div>
      <router-link to="/" class="back-button">← Volver al equipo</router-link>
    </div>

    <div class="profile-content">
      <!-- Sobre mí -->
      <article class="profile-about">
        <h3>Sobre mí</h3>
        <p>"{{ member.about }}"</p>
      </article>

      <!-- Proyectos -->
      <article class="profile-projects">
        <h3>Proyectos</h3>
        <div class="proyecto-imagenes">
          <img 
            v-for="(project, index) in member.projects" 
            :key="index"
            :src="project" 
            :alt="'Proyecto ' + (index + 1)"
            class="img-proyecto"
          >
        </div>
      </article>

      <!-- Habilidades -->
      <article class="profile-skills">
        <h3>Habilidades</h3>
        <div class="skills-list">
          <span v-for="skill in member.skills" :key="skill">{{ skill }}</span>
        </div>
      </article>

      <!-- Contacto -->
      <article class="profile-contact">
        <h3>Contacto</h3>
        <p>Email: <a :href="`mailto:${member.email}`">{{ member.email }}</a></p>
        
        <div class="footer-social">
          <a v-for="(url, platform) in member.social" 
             :key="platform"
             :href="url" 
             target="_blank" 
             rel="noopener noreferrer" 
             :aria-label="platform"
             class="social-link">
            <svg class="icono-red" viewBox="0 0 24 24">
              <path :d="getSocialIcon(platform)" />
            </svg>
          </a>
        </div>
      </article>
    </div>
  </section>

  <!-- Mensaje si no se encuentra el miembro -->
  <div v-else class="not-found">
    <h2>Miembro no encontrado</h2>
    <router-link to="/" class="back-button">Volver al equipo</router-link>
  </div>
</template>

<script>
import { teamMembers } from '@/data/team'

export default {
  name: 'MemberProfile',
  props: {
    id: {  // Recibimos el parámetro de la ruta como prop
      type: Number,
      required: true
    }
  },
  computed: {
    member() {
      // Convertir el id a número y buscar el miembro
      return teamMembers.find(m => m.id === Number(this.id))
    }
  },
  methods: {
    getSocialIcon(platform) {
      const icons = {
        instagram: "M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z",
        github: "M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12",
        linkedin: "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z",
        facebook: "M22.675 0H1.325C.593 0 0 .593 0 1.325v21.351C0 23.407.593 24 1.325 24H12.82v-9.294H9.692v-3.622h3.128V8.413c0-3.1 1.893-4.788 4.659-4.788 1.325 0 2.463.099 2.795.143v3.24l-1.918.001c-1.504 0-1.795.715-1.795 1.763v2.313h3.587l-.467 3.622h-3.12V24h6.116c.73 0 1.323-.593 1.323-1.325V1.325C24 .593 23.407 0 22.675 0z"
      }
      return icons[platform] || ""
    }
  }
}
</script>

<style scoped>
/* Tus estilos existentes aquí */

.not-found {
  text-align: center;
  padding: 4rem;
  color: #e0e0e0;
}

.not-found h2 {
  font-size: 2rem;
  margin-bottom: 2rem;
  color: #64b5f6;
}
</style>
<style scoped>
.profile-section {
  background: linear-gradient(145deg, #1a1a2e 0%, #16213e 100%);
  border-radius: 20px;
  padding: 3rem;
  margin: 2rem 0;
  border: 1px solid #333;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
  position: relative;
  overflow: hidden;
}

.profile-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, #64b5f6, #2196f3, #64b5f6);
}

.profile-header {
  display: flex;
  align-items: center;
  margin-bottom: 3rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid #333;
}

.profile-header img {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  margin-right: 2rem;
  border: 4px solid #64b5f6;
  box-shadow: 0 0 30px rgba(100, 181, 246, 0.3);
}

.profile-info {
  flex: 1;
}

.profile-header h2 {
  font-size: 2.5rem;
  color: #ffffff;
  margin-bottom: 0.5rem;
}

.profile-header h2 span {
  display: block;
  font-size: 1.5rem;
  color: #64b5f6;
  margin-top: 0.5rem;
  font-weight: 600;
}

.member-quote {
  font-style: italic;
  color: #b0b0b0;
  font-size: 1.1rem;
  margin-top: 0.5rem;
}

.back-button {
  padding: 0.8rem 1.5rem;
  background: linear-gradient(45deg, #64b5f6, #2196f3);
  color: white;
  text-decoration: none;
  border-radius: 8px;
  transition: all 0.3s ease;
  border: none;
  font-weight: 600;
}

.back-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(33, 150, 243, 0.4);
}

.profile-content {
  display: grid;
  gap: 2.5rem;
}

.profile-content article {
  padding: 2rem;
  background: rgba(30, 30, 48, 0.6);
  border-radius: 12px;
  border: 1px solid #333;
  transition: all 0.3s ease;
}

.profile-content article:hover {
  border-color: #64b5f6;
  transform: translateY(-2px);
}

.profile-content h3 {
  color: #64b5f6;
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
  border-bottom: 2px solid #64b5f6;
  padding-bottom: 0.5rem;
  font-weight: 600;
}

.profile-content p {
  color: #e0e0e0;
  line-height: 1.6;
  font-size: 1.1rem;
}

.proyecto-imagenes {
  display: flex;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.img-proyecto {
  width: 200px;
  height: 150px;
  object-fit: cover;
  border-radius: 8px;
  border: 2px solid #444;
  transition: all 0.3s ease;
}

.img-proyecto:hover {
  border-color: #64b5f6;
  transform: scale(1.05);
}

.skills-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.8rem;
}

.skills-list span {
  background: linear-gradient(45deg, #64b5f6, #2196f3);
  color: white;
  padding: 0.6rem 1.2rem;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.3s ease;
}

.skills-list span:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(33, 150, 243, 0.4);
}

.footer-social {
  display: flex;
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.social-link {
  padding: 0.8rem;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  transition: all 0.3s ease;
  border: 1px solid #444;
}

.social-link:hover {
  background: #64b5f6;
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(100, 181, 246, 0.4);
}

.icono-red {
  width: 24px;
  height: 24px;
  fill: #e0e0e0;
  transition: all 0.3s ease;
}

.social-link:hover .icono-red {
  fill: #ffffff;
}

.profile-contact a {
  color: #64b5f6;
  text-decoration: none;
  transition: color 0.3s ease;
}

.profile-contact a:hover {
  color: #2196f3;
  text-decoration: underline;
}
</style>