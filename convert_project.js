const { Project , Target, Block } = require("./sb-edit");

const fs = require("fs");
const path = require("path");
const axios = require('axios');


const projectURL = "https://scratch.mit.edu/projects/854666270/";




const postScratchProject = async (projectLink) => {
  try {
    const url = 'https://leopardjs.com/api/projects';  // Replace with the actual URL of the leopard.js API endpoint for posting projects

    // Create a payload object with the link to the Scratch project
    const payload = {
      link: projectLink
    };

    // Send the POST request
    const response = await axios.post(url, payload);

    // Handle the response
    console.log('Project posted successfully:', response.data);
  } catch (error) {
    console.error('Error posting project:', error);
  }
};

// Usage
//const scratchProjectLink = 'https://scratch.mit.edu/projects/123456789';  // Replace with the actual link to your Scratch project
postScratchProject(projectURL);

// const file = fs.readFileSync(path.join(__dirname, "my_project.sb3"));
// const project =  Project.fromSb3(file);

// console.log(project);



// fs.readFile("my_project.sb3", async (err, data) => {
//     if (err) throw err;
//     let project =  Project.fromSb3(data);
//     // Now you can access Scratch objects:
//     for (let target of project.targets) {
//       console.log(target.name, "has", target.blocks.size, "blocks");
//       for (let [id, block] of target.blocks) {
//         console.log("Block", id, "is a", block.opcode);
//       }
//     }
//   });

//project.toLeopard();


//console.log(project.toLeopard({ printWidth: 100 }));


