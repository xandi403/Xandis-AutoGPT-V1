self.abilities = AbilityRegister(self)
While AbilityRegister is studded with utility methods, two stand out. The list_abilities_for_prompt method curates and structures abilities for prompt integration. Conversely, run_ability operationalizes the designated ability, translating it from code to action.
An ability’s DNA comprises a function embellished with the @ability decorator and mandatorily paired with parameters, notably the agent and task_id.
@ability(
    name="write_file",
    description="Write data to a file",
    parameters=[
        {
            "name": "file_path",
            "description": "Path to the file",
            "type": "string",
            "required": True,
        },
        {
            "name": "data",
            "description": "Data to write to the file",
            "type": "bytes",
            "required": True,
        },
    ],
    output_type="None",
)
async def write_file(agent, task_id: str, file_path: str, data: bytes) -> None:
    pass
