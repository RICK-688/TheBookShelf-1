import {createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'
import author_book_create from "@/views/components/author_book_create";
import book_detail from "@/views/book_detail";
import about_us from "@/views/about_us";
import book_chatper from "@/views/book_chatper";
import user_book_case from "@/views/user_book_case";
import author_chapter_create from "@/views/author_chapter_create";
// import store from '../store/index'

const routes = createRouter({
    history: createWebHistory(),
    base: __dirname,
    routes: [
        {
            path: '/',
            name: 'Home',
            component: Home
    },
    {
      path: '/login',
      name: 'Login',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue')
    },
    {
      path: '/register',
      name: 'Register',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ '../views/registration.vue')
    },
    {
      path: '/payment/success',
      name: 'Payment_success',
      component: () => import('../views/Plan_success.vue'),
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/plan/',
      name: 'Payment',
      component: () => import('../views/plan.vue'),
        meta: {
            requireLogin: true
        }
    },
        {
            path: '/author/create',
            name: 'Author_create',
            component: author_book_create,
            meta: {
                requireLogin: true
            }
        },
        {
            path: '/author/chapter/create',
            name: 'chapter_create',
            component: author_chapter_create,
            meta: {
                requireLogin: true
            }
        },
        {
            path: '/book/',
            name: 'book_detail',
            component: book_detail,
            meta: {
                requireLogin: true
            }
        }, {
      path: '/book/chapter',
      name: 'chapter_detail',
      component: book_chatper,
      meta: {
        requireLogin: true
      }
        },
        {
            path: '/about/',
            name: 'about',
            component: about_us,
            meta: {
                requireLogin: true
            }
        },
        {
            path: '/bookcase/',
            name: 'bookcase',
            component: user_book_case,
            meta: {
                requireLogin: true
            }
        },

    ]
})

// routes.beforeEach((to, from, next) => {
//     if (to.meta.requireLogin && !store.state.isAuthenticated) {
//         console.log('login please')
//         next('/login')
//     } else {
//         next()
//     }
// })
export default routes;
