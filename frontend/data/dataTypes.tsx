 interface User {
    id: number,
    name: string,
    role: string,
    created_at: Date,
    last_login: Date,
    is_active: boolean
}

 interface Part {
    id: number,
    name: string,
    comment:string,
    created_at: Date,
    created_by: User,
}