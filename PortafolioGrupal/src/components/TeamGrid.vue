<template>
  <div class="team-container">
    <!-- Fila 1: JavaScript -->
    <div class="language-row">
      <!-- Tarjeta izquierda -->
      <div class="card-wrapper left-card">
        <MemberCard 
          v-if="getMemberByRole('Encargado de JavaScript', 0)"
          :member="getMemberByRole('Encargado de JavaScript', 0)"
          @member-click="goToMemberProfile"
        />
      </div>
      
      <!-- Lenguaje en el centro -->
      <div class="language-center">
        <div class="language-card javascript">
          <div class="language-icon">
            <svg viewBox="0 0 24 24">
              <path d="M0 0h24v24H0V0zm22.034 18.276c-.175-1.095-.888-2.015-3.003-2.873-.736-.345-1.554-.585-1.797-1.14-.091-.33-.105-.51-.046-.705.15-.646.915-.84 1.515-.66.39.12.75.42.976.9 1.034-.676 1.034-.676 1.755-1.125-.27-.337-.404-.482-.586-.621-.378-.27-.93-.42-1.42-.42-.825.0-1.455.345-1.846.99-.72 1.2-.515 2.97.795 3.75 1.14.63 2.82.825 3.15 1.455.36.705.03 1.56-.75 1.95-.66.33-1.56.33-2.25-.09l-.75.96c.45.42 1.08.66 1.83.66 1.14.0 2.01-.51 2.43-1.38.33-.87.18-1.83-.45-2.43zM8.954 16.23c-.165.0-.33-.03-.48-.09-.405-.18-.57-.48-.57-.93.0-.69.495-.96 1.395-1.26.93-.3 2.13-.66 2.13-1.74.0-.84-.66-1.38-1.74-1.38-.81.0-1.5.27-1.95.81-.27.33-.39.69-.39 1.14h-1.5c0-.63.165-1.2.495-1.68.57-.78 1.59-1.26 2.85-1.26 1.65.0 2.97.75 2.97 2.22.0 1.05-.63 1.65-1.8 2.1-.87.33-1.29.54-1.47.81-.18.27-.21.45-.21.75.0 .42.27.75.75.75.39.0 .75-.15 1.02-.45.27-.3.48-.66 1.38-.66h1.29c-.18 1.08-.84 1.56-2.25 1.56z"/>
            </svg>
          </div>
          <h3>JavaScript</h3>
          <p>Desarrollo Frontend y Backend</p>
          <div class="members-count">
            {{ getMembersCountByRole('Encargado de JavaScript') }} miembros
          </div>
        </div>
      </div>

      <!-- Tarjeta derecha -->
      <div class="card-wrapper right-card">
        <MemberCard 
          v-if="getMemberByRole('Encargado de JavaScript', 1)"
          :member="getMemberByRole('Encargado de JavaScript', 1)"
          @member-click="goToMemberProfile"
        />
      </div>
    </div>

    <!-- Fila 2: Python -->
    <div class="language-row">
      <!-- Tarjeta izquierda -->
      <div class="card-wrapper left-card">
        <MemberCard 
          v-if="getMemberByRole('Encargado de Python', 0)"
          :member="getMemberByRole('Encargado de Python', 0)"
          @member-click="goToMemberProfile"
        />
      </div>
      
      <!-- Lenguaje en el centro -->
      <div class="language-center">
        <div class="language-card python">
          <div class="language-icon">
            <svg viewBox="0 0 24 24">
              <path d="M9.583 17.321c-.447 0-.82-.126-1.12-.38-.3-.252-.45-.57-.45-.95 0-.38.15-.697.45-.95.3-.253.673-.38 1.12-.38.447 0 .82.127 1.12.38.3.253.45.57.45.95 0 .38-.15.698-.45.95-.3.254-.673.38-1.12.38zm-.18-8.392c-.447 0-.82-.126-1.12-.38-.3-.252-.45-.57-.45-.95 0-.38.15-.697.45-.95.3-.253.673-.38 1.12-.38.447 0 .82.127 1.12.38.3.253.45.57.45.95 0 .38-.15.698-.45.95-.3.254-.673.38-1.12.38z"/>
              <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1.5 16c-.83 0-1.5-.67-1.5-1.5v-2.5c0-.83.67-1.5 1.5-1.5h3c.83 0 1.5.67 1.5 1.5v2.5c0 .83-.67 1.5-1.5 1.5h-3zm6.5-6c-.83 0-1.5-.67-1.5-1.5v-2.5c0-.83.67-1.5 1.5-1.5h1.5c.83 0 1.5.67 1.5 1.5v2.5c0 .83-.67 1.5-1.5 1.5H17z"/>
            </svg>
          </div>
          <h3>Python</h3>
          <p>Data Science & Backend</p>
          <div class="members-count">
            {{ getMembersCountByRole('Encargado de Python') }} miembros
          </div>
        </div>
      </div>

      <!-- Tarjeta derecha -->
      <div class="card-wrapper right-card">
        <MemberCard 
          v-if="getMemberByRole('Encargado de Python', 1)"
          :member="getMemberByRole('Encargado de Python', 1)"
          @member-click="goToMemberProfile"
        />
      </div>
    </div>

    <!-- Fila 3: Java -->
    <div class="language-row">
      <!-- Tarjeta izquierda -->
      <div class="card-wrapper left-card">
        <MemberCard 
          v-if="getMemberByRole('Encargado de Java', 0)"
          :member="getMemberByRole('Encargado de Java', 0)"
          @member-click="goToMemberProfile"
        />
      </div>
      
      <!-- Lenguaje en el centro -->
      <div class="language-center">
        <div class="language-card java">
          <div class="language-icon">
            <svg viewBox="0 0 24 24">
              <path d="M9.37 17.16c-.82.24-1.72.36-2.67.36-1.13 0-2.17-.17-3.11-.5.44-1.04 1.06-1.96 1.84-2.75.78-.78 1.7-1.4 2.74-1.84-.33.94-.5 1.98-.5 3.11 0 .95.12 1.85.36 2.67l.34-.05zm2.63-2.63c-.24.82-.36 1.72-.36 2.67 0 1.13.17 2.17.5 3.11-1.04-.44-1.96-1.06-2.75-1.84-.78-.78-1.4-1.7-1.84-2.74.94.33 1.98.5 3.11.5.95 0 1.85-.12 2.67-.36l-.33-.34zM12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"/>
            </svg>
          </div>
          <h3>Java</h3>
          <p>Enterprise Applications</p>
          <div class="members-count">
            {{ getMembersCountByRole('Encargado de Java') }} miembros
          </div>
        </div>
      </div>

      <!-- Tarjeta derecha -->
      <div class="card-wrapper right-card">
        <MemberCard 
          v-if="getMemberByRole('Encargado de Java', 1)"
          :member="getMemberByRole('Encargado de Java', 1)"
          @member-click="goToMemberProfile"
        />
      </div>
    </div>

    <!-- Fila 4: Base de Datos -->
    <div class="language-row single-card">
      <div class="card-wrapper center-card">
        <MemberCard 
          v-if="getMemberByRole('Encargado de Base de Datos', 0)"
          :member="getMemberByRole('Encargado de Base de Datos', 0)"
          @member-click="goToMemberProfile"
        />
      </div>
      
      <!-- Lenguaje en el centro -->
      <div class="language-center">
        <div class="language-card database">
          <div class="language-icon">
            <svg viewBox="0 0 24 24">
              <path d="M12 3C7.58 3 4 4.79 4 7s3.58 4 8 4 8-1.79 8-4-3.58-4-8-4zm0 6c-3.31 0-6-.9-6-2s2.69-2 6-2 6 .9 6 2-2.69 2-6 2zm6 1.5v.5c0 1.1-2.69 2-6 2s-6-.9-6-2v-.5c0 .66 1.34 1.25 3.33 1.58.94.2 1.95.32 2.67.32s1.73-.12 2.67-.32c1.99-.33 3.33-.92 3.33-1.58zm0 2.5v.5c0 1.1-2.69 2-6 2s-6-.9-6-2v-.5c0 .66 1.34 1.25 3.33 1.58.94.2 1.95.32 2.67.32s1.73-.12 2.67-.32c1.99-.33 3.33-.92 3.33-1.58zm0 2.5v.5c0 1.1-2.69 2-6 2s-6-.9-6-2v-.5c0 .66 1.34 1.25 3.33 1.58.94.2 1.95.32 2.67.32s1.73-.12 2.67-.32c1.99-.33 3.33-.92 3.33-1.58z"/>
            </svg>
          </div>
          <h3>Base de Datos</h3>
          <p>Data Management & Storage</p>
          <div class="members-count">
            {{ getMembersCountByRole('Encargado de Base de Datos') }} miembro
          </div>
        </div>
      </div>

      <div class="card-wrapper empty-card"></div>
    </div>
  </div>
</template>

<script>
import { teamMembers } from '@/data/team'
import MemberCard from './MemberCard.vue'

export default {
  name: 'TeamGrid',
  components: {
    MemberCard
  },
  data() {
    return {
      teamMembers
    }
  },
  methods: {
    goToMemberProfile(memberId) {
      this.$router.push(`/member/${memberId}`)
    },
    
    getMemberByRole(role, index) {
      const members = this.teamMembers.filter(member => member.role === role)
      return members[index] || null
    },
    
    getMembersCountByRole(role) {
      return this.teamMembers.filter(member => member.role === role).length
    }
  }
}
</script>

<style scoped>
.team-container {
  display: flex;
  flex-direction: column;
  gap: 3rem;
  padding: 2rem 0;
}

.language-row {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 2rem;
  min-height: 300px;
}

.language-row.single-card {
  grid-template-columns: 1fr auto 1fr;
}

.card-wrapper {
  display: flex;
  justify-content: center;
}

.left-card {
  justify-content: flex-end;
}

.right-card {
  justify-content: flex-start;
}

.center-card {
  justify-content: center;
}

.empty-card {
  visibility: hidden;
}

.language-center {
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 250px;
}

.language-card {
  background: linear-gradient(145deg, #1e1e2e 0%, #252536 100%);
  border: 2px solid;
  border-radius: 20px;
  padding: 2rem;
  text-align: center;
  min-width: 200px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.language-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, currentColor, transparent);
}

.language-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4);
}

.language-card.javascript {
  border-color: #f7df1e;
  color: #f7df1e;
}

.language-card.python {
  border-color: #3776ab;
  color: #3776ab;
}

.language-card.java {
  border-color: #ed8b00;
  color: #ed8b00;
}

.language-card.database {
  border-color: #336791;
  color: #336791;
}

.language-icon {
  width: 60px;
  height: 60px;
  margin: 0 auto 1rem;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.language-icon svg {
  width: 30px;
  height: 30px;
  fill: currentColor;
}

.language-card h3 {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: #ffffff;
}

.language-card p {
  color: #b0b0b0;
  margin-bottom: 1rem;
  font-size: 0.9rem;
}

.members-count {
  background: rgba(255, 255, 255, 0.1);
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
  color: currentColor;
}

/* Responsive */
@media (max-width: 1024px) {
  .language-row {
    grid-template-columns: 1fr;
    gap: 1.5rem;
    text-align: center;
  }
  
  .left-card, .right-card, .center-card {
    justify-content: center;
  }
  
  .language-center {
    order: -1;
  }
}

@media (max-width: 768px) {
  .team-container {
    gap: 2rem;
  }
  
  .language-card {
    padding: 1.5rem;
    min-width: 180px;
  }
}
</style>