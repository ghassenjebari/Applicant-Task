import axios from 'axios'

export const getUsers = async (): Promise<User[]> => {
    const { data } = await axios.get(
        process.env.NEXT_PUBLIC_HOST + '/users'
    )
    return data
}

export const createPart = async (part: { name: string; comment: string }) => {
    await axios.post(process.env.NEXT_PUBLIC_HOST + "/parts", part);
  };
  
export const getParts = async (): Promise<Part[]> => {
    const { data } = await axios.get(
        process.env.NEXT_PUBLIC_HOST + '/parts'
    )
    return data
  
}

// Fetch a part by ID
export const getPartById = async (id: number) => {
    const { data } = await axios.get(`${process.env.NEXT_PUBLIC_HOST}/parts/${id}`);
    return data;
  };
  
  // Update a part by ID
  export const updatePart = async (id: number, updateData: { name: string; comment: string }) => {
    await axios.patch(`${process.env.NEXT_PUBLIC_HOST}/parts/${id}`, updateData);
  };