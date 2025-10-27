<template>
  <div id="app">
    <!-- 导航栏 -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
      <div class="container">
        <router-link class="navbar-brand" to="/">
          <i class="fas fa-book"></i> 百科系统
        </router-link>
        
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span class="navbar-toggler-icon"></span>
        </button>
        
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <router-link class="nav-link" to="/">
                <i class="fas fa-home"></i> 首页
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/entries">
                <i class="fas fa-list"></i> 词条列表
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/categories">
                <i class="fas fa-folder"></i> 分类管理
              </router-link>
            </li>
          </ul>
          
          <!-- 搜索框 -->
          <form class="d-flex" @submit.prevent="searchEntries">
            <div class="input-group">
              <input 
                v-model="searchQuery" 
                type="search" 
                class="form-control" 
                placeholder="搜索词条..."
                aria-label="搜索">
              <button class="btn btn-outline-light" type="submit">
                <i class="fas fa-search"></i>
              </button>
            </div>
          </form>
        </div>
      </div>
    </nav>
    
    <!-- 主要内容 -->
    <main class="container mt-4">
      <router-view />
    </main>
    
    <!-- 页脚 -->
    <footer class="bg-light mt-5 py-4">
      <div class="container text-center">
        <p class="mb-0 text-muted">
          <i class="fas fa-code"></i> 使用 Vue.js 构建的百科系统
        </p>
      </div>
    </footer>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

export default {
  name: 'App',
  setup() {
    const searchQuery = ref('')
    const router = useRouter()
    
    const searchEntries = () => {
      if (searchQuery.value.trim()) {
        router.push(`/entries?search=${encodeURIComponent(searchQuery.value)}`)
      }
    }
    
    return {
      searchQuery,
      searchEntries
    }
  }
}
</script>

<style>
.navbar-brand {
  font-weight: bold;
}

.router-link-active {
  font-weight: bold;
}

#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

main {
  flex: 1;
}

footer {
  margin-top: auto;
}
</style>