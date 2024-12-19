import axios from 'axios'

export const getUsers = async (): Promise<User[]> => {
    const { data } = await axios.get(
        process.env.NEXT_PUBLIC_HOST + '/users'
    )
    return data
}

export const getParts = async (): Promise<Part[]> => {
    const { data } = await axios.get(
        process.env.NEXT_PUBLIC_HOST + '/parts'
    )
    return data
}