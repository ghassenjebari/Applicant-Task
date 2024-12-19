import { getParts } from "@/data/dataHandler"
import { List } from "@mantine/core"
import { useEffect, useState } from "react"

const PartList = () => {
    const [parts, setParts] = useState<Part[]>([])

    useEffect(() => {
        const initData = async () => {
            const parts = await getParts()
            setParts(parts)
        }
        initData()
    }, [])

    return (
        <List>
            {parts.map((part, idx) => {
                return (
                    <List.Item key={idx}>
                        ID: {part.id} { }
                        Name: {part.name} { }
                        Created by: {part.created_by.name} { }
                    </List.Item>
                )
            })}
        </List>
    )
}
export default PartList