import axios from 'axios'

// 创建axios实例
const api = axios.create({
  baseURL: '/api',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// 请求拦截器
api.interceptors.request.use(
  (config) => {
    // 可以在这里添加认证token等
    console.log('发送请求:', config.method?.toUpperCase(), config.url)
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// 响应拦截器
api.interceptors.response.use(
  (response) => {
    return response.data
  },
  (error) => {
    console.error('API请求错误:', error)
    return Promise.reject(error)
  }
)

// 词条相关API
export const entryApi = {
  // 获取词条列表
  getEntries: (params = {}) => api.get('/entries/', { params }),
  
  // 获取词条详情
  getEntry: (id) => api.get(`/entries/${id}/`),
  
  // 创建词条
  createEntry: (data) => api.post('/entries/', data),
  
  // 更新词条
  updateEntry: (id, data) => api.put(`/entries/${id}/`, data),
  
  // 删除词条
  deleteEntry: (id) => api.delete(`/entries/${id}/`),
  
  // 搜索词条
  searchEntries: (query) => api.get('/entries/', { params: { search: query } })
}

// 分类相关API
export const categoryApi = {
  // 获取分类列表
  getCategories: () => api.get('/categories/'),
  
  // 获取分类详情
  getCategory: (id) => api.get(`/categories/${id}/`),
  
  // 创建分类
  createCategory: (data) => api.post('/categories/', data),
  
  // 更新分类
  updateCategory: (id, data) => api.put(`/categories/${id}/`, data),
  
  // 删除分类
  deleteCategory: (id) => api.delete(`/categories/${id}/`),
  
  // 获取分类下的词条
  getCategoryEntries: (id) => api.get(`/categories/${id}/entries/`)
}

// 统计相关API
export const statsApi = {
  // 获取系统统计
  getStats: () => api.get('/stats/')
}

export default api