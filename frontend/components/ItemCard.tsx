import { Card, Avatar, Text, Group, Stack,Button } from "@mantine/core";

interface ItemCardProps {
    id: number;
    name: string;
    description?: string; 
    createdBy?: string; 
    type: "user" | "part";
    onEdit?: (id: number) => void; 
}

const ItemCard = ({ id, name, description, createdBy, type, onEdit }: ItemCardProps) => {
    return (
        <Card shadow="sm" padding="lg" radius="md" className="item-card">
            <Stack spacing="sm" align="center"> 
                <Avatar radius="xl">{name.charAt(0).toUpperCase()}</Avatar>

                <Text weight={700} align="center">{name}</Text>
                
                {description && (
                    <Text size="sm" align="center">
                        {description}
                    </Text>
                )}


                 {type === "part" && createdBy && (
                    <Text size="xs" align="center" color="dimmed">
                        Created by: {createdBy}
                    </Text>
                )}

               
                {type === "part" && (

                    <div className="edit-button-container">
                    <Button color="blue" onClick={() => onEdit?.(id)} size="xs" className="glass-button">
                        Edit
                    </Button>
                </div>  
                )}

            </Stack>
        </Card>
    );
};

export default ItemCard;
