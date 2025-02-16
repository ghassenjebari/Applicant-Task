import { getParts } from "@/data/dataHandler";
import { useEffect, useState } from "react";
import { Modal, Button, Loader, Stack, Title, Text, TextInput, Group, Paper } from "@mantine/core";
import AddPartForm from "@/components/addPartForm";
import ModifyPartForm from "@/components/modifyPartForm";
import ItemCard from "@/components/ItemCard";




const PartList = () => {
    const [parts, setParts] = useState<Part[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [opened, setOpened] = useState(false);
    const [openedModifyModal, setOpenedModifyModal] = useState(false);
    const [selectedPartId, setSelectedPartId] = useState<number | null>(null);
    const [searchTerm, setSearchTerm] = useState<string>("");
    const [filteredParts, setFilteredParts] = useState<Part[]>([]);


    

    useEffect(() => {
        const fetchParts = async () => {
            setLoading(true);
            try {
                const partsData = await getParts();
                setParts(partsData);
                setFilteredParts(partsData);
            } catch (error) {
                console.error("Error fetching parts:", error);
            } finally {
                setLoading(false);

            }
        };
        fetchParts();
    }, []);

    useEffect(() => {
        const filtered = parts.filter(part =>
            part.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
            part.comment.toLowerCase().includes(searchTerm.toLowerCase())
        );
        setFilteredParts(filtered);
    }, [searchTerm, parts])
     ;


    const handleModifyPart = (id: number) => {
        setSelectedPartId(id);
        setOpenedModifyModal(true);
    };


    return (


        <div className="main-content">

        
            <div className="search-bar-container">
                <TextInput
                    placeholder="🔍 Search parts..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    style={{ width: "500px" }}
                />
                <Button
                    color="blue"
                    onClick={() => setOpened(true)}
                    className="add-button glass-button"
                >
                    ➕ Add Part
                </Button>
            </div>

            <Modal
                opened={opened}
                onClose={() => setOpened(false)}
                centered
                withCloseButton={false}
                padding="lg"
                classNames={{ content: "glass-modal" }} 
                >
                <Title order={3} align="center" className="modal-title">
                    Add a New Part
                </Title>

                <AddPartForm onPartAdded={() => {
                    setLoading(true);
                    getParts().then((partsData) => {
                        setParts(partsData);
                        setFilteredParts(partsData);
                        setLoading(false);
                        setOpened(false);
                    });
                }} />
            </Modal>

            <Modal
              centered  


              withCloseButton={false} 

                opened={openedModifyModal}
                onClose={() => { setOpenedModifyModal(false); setSelectedPartId(null); }}
   
  classNames={{ content: "glass-modal" }} 
  styles={{ content: { maxWidth: "400px" } }}  


            >
                <Title order={3} align="center" className="modal-title">
  Modify Part
</Title>
                {selectedPartId && (
                    
                    <ModifyPartForm
                        partId={selectedPartId}
                        onPartUpdated={() => {
                            setLoading(true);
                            getParts().then((partsData) => {
                                setParts(partsData);
                                setFilteredParts(partsData);
                                setLoading(false);
                                setOpenedModifyModal(false);
                                setSelectedPartId(null);
                                
                            });
                        }}
                        onClose={() => { setOpenedModifyModal(false); setSelectedPartId(null); }}
                    />
                )}
            </Modal>
               
                

            {loading ? (
                <Loader color="blue" size="lg" />
            ) : filteredParts.length === 0 ? (
                <Text color="dimmed" size="md">No part found.</Text>
            ) : (
                <div className="part-grid">
                    {filteredParts.map((part) => (
                        <ItemCard
                            key={part.id}
                            id={part.id}
                            name={part.name}
                            description={part.comment}
                            createdBy={part.created_by.name}
                            type="part"
                            onEdit={handleModifyPart}
                        />
                    ))}
                </div>
            )}
            
        </div>
    );

                        

        
};



export default PartList;
