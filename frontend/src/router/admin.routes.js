
export default [
  {
    path: '/admin',
    component: () => import('@/views/admin/AdminLayoutPage.vue'),
    meta: { role: 'admin' },
    children:[
      {
        path:'dashboard',
        name:'admin-dashboard',
        component:()=> import('@/views/admin/DashboardPage.vue')
      },
      {
        path:'doctors',
        component:()=>import('@/views/admin/doctors/DoctorLayoutPage.vue'),
        children:[
          {
            path:"",
            name:'doctors-list',
            component:()=>import('@/views/admin/doctors/DoctorsListPage.vue')
          }
          ,
          {
            path:'create',
            name:'add-doctor',
            component:()=>import('@/views/admin/doctors/AddDoctorPage.vue')
          }
        ]
      },
      {
        path:"departments",
        component:()=>import('@/views/admin/departments/DepartmentLayoutPage.vue'),
        children:[
          {
            path:"",
            name:'departmentList-admin',
            component:()=>import('@/views/admin/departments/DepartmentsPage.vue')
          },
          {
            path:"create",
            name:'addDepartment-admin',
            component:()=>import('@/views/admin/departments/AddDepartmentPage.vue')
          }
        ]
      },
      {
        path:"appointments",
        name:"appointments-admin",
        component:()=>import('@/views/admin/AppointmentsPage.vue'),
        
      },
      {
        path:"patients",
        name:"patients-admin",
        component:()=>import('@/views/admin/PatientsPage.vue'),
        
      }
    ]
  }
]
