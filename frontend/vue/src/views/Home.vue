<template>
  <div class="home">
    <!-- 欢迎区域 -->
    <div class="row align-items-center mb-5">
      <div class="col-lg-6">
        <h1 class="display-4 fw-bold text-primary mb-3">
          <i class="fas fa-book me-3"></i>百科系统
        </h1>
        <p class="lead text-muted mb-4">
          一个现代化的知识管理平台，使用Vue.js构建的前端界面
        </p>
        <div class="d-grid gap-2 d-md-flex">
          <router-link to="/entries" class="btn btn-primary btn-lg">
            <i class="fas fa-list me-2"></i>浏览词条
          </router-link>
          <router-link to="/categories" class="btn btn-outline-primary btn-lg">
            <i class="fas fa-folder me-2"></i>分类管理
          </router-link>
        </div>
      </div>
      <div class="col-lg-6 text-center">
        <i class="fas fa-book-open fa-10x text-primary opacity-25"></i>
      </div>
    </div>

    <!-- 功能特性 -->
    <div class="row mb-5">
      <div class="col-12">
        <h2 class="text-center mb-4">系统特性</h2>
        <div class="row">
          <div class="col-md-4 mb-4">
            <div class="card h-100 border-0 shadow-sm">
              <div class="card-body text-center">
                <i class="fas fa-search fa-3x text-primary mb-3"></i>
                <h5 class="card-title">智能搜索</h5>
                <p class="card-text text-muted">快速搜索和筛选词条内容，支持关键词匹配</p>
              </div>
            </div>
          </div>
          <div class="col-md-4 mb-4">
            <div class="card h-100 border-0 shadow-sm">
              <div class="card-body text-center">
                <i class="fas fa-layer-group fa-3x text-success mb-3"></i>
                <h5 class="card-title">分类管理</h5>
                <p class="card-text text-muted">完善的分类系统，便于知识组织和查找</p>
              </div>
            </div>
          </div>
          <div class="col-md-4 mb-4">
            <div class="card h-100 border-0 shadow-sm">
              <div class="card-body text-center">
                <i class="fas fa-mobile-alt fa-3x text-info mb-3"></i>
                <h5 class="card-title">响应式设计</h5>
                <p class="card-text text-muted">完美适配各种设备，提供一致的用户体验</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 快速统计 -->
    <div class="row">
      <div class="col-12">
        <h2 class="text-center mb-4">数据统计</h2>
        <div class="row text-center">
          <div class="col-md-3 mb-3">
            <div class="card bg-primary text-white">
              <div class="card-body">
                <h3 class="card-title">{{ stats.totalEntries || 0 }}</h3>
                <p class="card-text">总词条数</p>
              </div>
            </div>
          </div>
          <div class="col-md-3 mb-3">
            <div class="card bg-success text-white">
              <div class="card-body">
                <h3 class="card-title">{{ stats.totalCategories || 0 }}</h3>
                <p class="card-text">分类数量</p>
              </div>
            </div>
          </div>
          <div class="col-md-3 mb-3">
            <div class="card bg-info text-white">
              <div class="card-body">
                <h3 class="card-title">{{ stats.totalWords || 0 }}</h3>
                <p class="card-text">总字数</p>
              </div>
            </div>
          </div>
          <div class="col-md-3 mb-3">
            <div class="card bg-warning text-white">
              <div class="card-body">
                <h3 class="card-title">{{ stats.avgWords || 0 }}</h3>
                <p class="card-text">平均字数</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import api from '../utils/api'

export default {
  name: 'Home',
  setup() {
    const stats = ref({})

    const fetchStats = async () => {
      try {
        // 这里可以调用API获取统计数据
        stats.value = {
          totalEntries: 0,
          totalCategories: 0,
          totalWords: 0,
          avgWords: 0
        }
      } catch (error) {
        console.error('获取统计数据失败:', error)
      }
    }

    onMounted(() => {
      fetchStats()
    })

    return {
      stats
    }
  }
}
</script>

<style scoped>
.home {
  min-height: 70vh;
}

.card {
  transition: transform 0.2s;
}

.card:hover {
  transform: translateY(-5px);
}
</style>