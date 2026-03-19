import { ref, computed } from 'vue'

function getNestedValue(obj, path) {
    return path.split('.').reduce((acc, key) => acc?.[key], obj)
}

export function useSearchFilter(data, fields, filters = {}) {
    const searchQuery = ref('')

    const filteredData = computed(() => {
        let result = data.value

        
        if (searchQuery.value) {
            result = result.filter(item =>
                fields.some(field => {
                    const value = getNestedValue(item, field)
                    return String(value || '')
                        .toLowerCase()
                        .includes(searchQuery.value.toLowerCase())
                })
            )
        }

        
       
        Object.keys(filters).forEach(key => {
            const filterValue = filters[key].value

            if (Array.isArray(filterValue) && filterValue.length > 0) {
               
                result = result.filter(item => {
                    const value = getNestedValue(item, key)
                    return filterValue
                        .map(v => v.toLowerCase())
                        .includes(String(value).toLowerCase())
                })
            } 
            else if (filterValue) {
           
                result = result.filter(item => {
                    const value = getNestedValue(item, key)
                    return String(value) === String(filterValue)
                })
            }
        })

        return result
    })

    return {
        searchQuery,
        filteredData
    }
}